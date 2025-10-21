import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { MessageService } from 'primeng/api';
import { StService } from 'src/app/demo/service/st.service';
import { LayoutService } from 'src/app/layout/service/app.layout.service';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styles: [`
        :host ::ng-deep .pi-eye,
        :host ::ng-deep .pi-eye-slash {
            transform:scale(1.6);
            margin-right: 1rem;
            color: var(--primary-color) !important;
        }
    `],
    providers: [MessageService],
})
export class LoginComponent implements OnInit {

    model: any[] = [];

    i: any;
    i1: any;
    i2: any;
    i3: any;
    i4: any;
    i5: any;
    i6: any;
    i7: any;
    i8: any;
    i9: any;
    i10: any;
    i11: any;
    langs: any;

    valCheck: string[] = ['remember'];

    password!: string;

    email: string;

    Language: any;
    constructor(public layoutService: LayoutService, private http: StService, private msgService: MessageService, private router: Router) { }

    ngOnInit(): void {
        this.http.removeString('user_id');
        this.http.removeString('role');
        this.http.removeString('email');
        this.http.removeString('name');
    };

    login() {
        let obj = {
            email: this.email,
            password: this.password
        }
        this.loginUser(obj);
    }

    loginUser(obj: any) {
        this.http.loginUser(obj).subscribe(
            (res: any) => this.handleLoginResponse(res),
            (err: any) => this.handleError(err, 'Internet Server Error')
        );
    }

    handleLoginResponse(res: any) {
        if (res.con) {
            this.msgService.add({ key: 'tst', severity: 'success', summary: JSON.stringify(res.msg), detail: 'Login Successful' });
            this.storeUserData(res.data);
            // this.handleAdminLogin(res.data);
        } else {
            this.msgService.add({ key: 'tst', severity: 'error', summary: 'Error Message', detail: 'Login Error' });
        }
    }

    storeUserData(data: any) {
        this.http.setString('user_id', String(data.user_id));
        this.http.setString('email', String(data.email));
        this.http.setString('name', String(data.name));
        this.http.setString('phone', String(data.phone));
        this.http.setString('address', String(data.address));
        this.http.setString('role', String(data.role.name ));
        console.log(data)
        this.router.navigateByUrl('/');
    }

    handleError(error: any, detail: string) {
        this.msgService.add({ key: 'tst', severity: 'error', summary: JSON.stringify(error), detail });
    }
}
